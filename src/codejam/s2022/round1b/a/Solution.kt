package codejam.s2022.round1b.a

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
    val d = readLine().split(" ").map { it.toInt() }

    var li = 0
    var ri = n - 1

    var c = 0
    var highest = 0
    var result = 0

    while (c < n) {
        if (d[li] < d[ri] || li == ri) {
            if (d[li] >= highest) {
                result += 1
            }
            highest = maxOf(highest, d[li])
            c++
            li++
        } else {
            if (d[ri] >= highest) {
                result += 1
            }
            highest = maxOf(highest, d[ri])
            c++
            ri--
        }
    }

    println("Case #${t}: $result")
}
