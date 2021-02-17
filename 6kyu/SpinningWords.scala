object SpinningWords {
    def spinWords(sentence: String): String = {
        sentence
        .split(" ")
        .map(i => 
            if (i.length >= 5) i.reverse 
            else i
        )
        .mkString(" ")
    }
}