import echonest.audio as audio
from pyechonest import config
import sys

config.ECHO_NEST_API_KEY = "get a key here http://developer.echonest.com/account/register"

class Node:
  left = None
  right = None 
  def __init__(self, key, value):
    self.key = key
    self.value = value

class Tree:
  root = None 

  def add(self, key, value):
    if self.root == None:
      self.root = Node(key, value)
    else:
      self._add(self.root, key, value)

  def _add(self, node, key, value):
    branch = 'left'
    if node.key > key:
      branch = 'right'

    if getattr(node, branch):
      self._add(getattr(node, branch), key, value)
    else:
      setattr(node, branch, Node(key, value))

  def traverse(self, kind, visit):
    # http://en.wikipedia.org/wiki/Tree_traversal
    # kind is one of [preorder, inorder, postorder]

    if self.root:
      getattr(self, kind)(self.root, visit)
   
  def preorder(self, node, visit):
    visit(node.key, node.value)
    if node.left:
      self.inorder(node.left, visit)
    if node.right:
      self.inorder(node.right, visit)
 
  def inorder(self, node, visit):
    if node.left:
      self.inorder(node.left, visit)
    visit(node.key, node.value)
    if node.right:
      self.inorder(node.right, visit)

  def postorder(self, node, visit):
    if node.left:
      self.inorder(node.left, visit)
    if node.right:
      self.inorder(node.right, visit)
    visit(node.key, node.value)

def inorderTest():
  keys = ["ma", "ro", "zin", "ko", "aq", "er", "se", "ca", "pi", "ty", "ge", "me", "mo"]
  t = Tree()
  print("original: ")
  for k in keys:
    sys.stdout.write(k + ", ")
    t.add(k, len(k))

  def visit(k, v):
    sys.stdout.write(k + ", ")

  print("\npre:")
  t.traverse('preorder', visit)
  print("")
  print("in:")
  t.traverse('inorder', visit)
  print("")
  print("post:")
  t.traverse('postorder', visit)
  print("")


def inorder():
  audio_file = audio.LocalAudioFile("../zambi.mp3")
  parts = audio_file.analysis.segments

  t = Tree()
  for p in parts:
    # start, duration, timbre, loudness_begin, loudness_max, time_loudness_max or loudness_end
    t.add(p.loudness_max, p)

  ordered = []
  def visit(k, v):
    ordered.append(v)

  t.traverse('postorder', visit)

  # And render the list as a new audio file!
  audio.getpieces(audio_file, ordered).encode("../inorder.mp3")


if __name__ == "__main__":
  # inorderTest()
  inorder()
