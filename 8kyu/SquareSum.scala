object SquareSum {

  def squareSum(xs: List[Int]): Int = {
    var acc = 0
    xs.map(i => acc += i*i)
    acc
  }
}