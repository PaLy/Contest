package codejam.s2022.round1a.c

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
    val n = readLine().toInt()
    val s = readLine().split(" ").map { it.toInt() }.sorted()

    var result = 0
    var index = 1
    s.forEach {
        if (it >= index) {
            result += 1
            index += 1
        }
    }

    println("Case #${t}: $result")
}
