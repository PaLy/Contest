package codejam.s2022.round1a.a

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
    val s = readLine()
    var res = ""

    var lastChar = s[0]
    res += lastChar
    var same = ""
    same += lastChar

    for (i in 1 until s.length) {
        val curChar = s[i]
        if (curChar < lastChar) {
            same = curChar.toString()
        } else if (curChar > lastChar) {
            res += same
            same = curChar.toString()
        } else {
            same += curChar
        }
        res += curChar
        lastChar = curChar
    }

    println("Case #$t: $res")
}
