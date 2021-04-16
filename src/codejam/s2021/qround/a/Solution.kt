package codejam.s2021.qround.a

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
    var l = readLine().split(" ").map { it.toInt() }

    var cost = 0

    for (i in 0 until n - 1) {
        val j = l.subList(i, n).withIndex().minByOrNull { it.value }!!.index + i

        l = l.subList(0, i) + l.subList(i, j + 1).asReversed() + l.subList(j + 1, n)

        cost += j - i + 1
    }

    println("Case #$t: $cost")
}
