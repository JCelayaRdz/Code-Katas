object Kata {
  def grow(xs: List[Long]): Long = xs.reduce((acc,i) => acc * i)
}