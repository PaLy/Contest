package codejam.s2022.qround.a

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream

fun main() {
    solve(System.`in`, System.out)
}

fun solve(inputStream: InputStream, out: PrintStream) {
    val reader = BufferedReader(InputStreamReader(inputStream))
    val printer = PrintStream(out)
    val readLine = { reader.readLine() }
    val println = { it: String -> printer.println(it) }

    val t = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    val (r, c) = readLine().split(" ").map { it.toInt() }

    println("Case #$t:")

    var line1 = ".."
    for (i in 1 until c) line1 += "+-"
    line1 += "+"
    println(line1)

    var line2 = "."
    for (i in 1..c) line2 += ".|"
    println(line2)

    var line3 = ""
    for (i in 1..c) line3 += "+-"
    line3 += "+"
    println(line3)

    for (i in 1 until r) {
        var line = ""
        for (j in 1..c) line += "|."
        line += "|"
        println(line)

        line = ""
        for (j in 1..c) line += "+-"
        line += "+"
        println(line)
    }
}
