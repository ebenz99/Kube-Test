num = Channel.from(2..5)

process test {
  input:
  val x from num

  """
  sleep 90
  python3 app/app.py
  """
}
