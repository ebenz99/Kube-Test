num = Channel.from(4..5)

process test {
  input:
  val x from num

  """
  sleep 2
  """
}
