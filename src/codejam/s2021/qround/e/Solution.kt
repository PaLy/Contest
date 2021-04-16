package codejam.s2021.qround.e

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
    val p = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println, p)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit, p: Int) {
    val a = (1..100).map { readLine() }.toList()

    val q = (0 until 10000).map { qi ->
        (0 until 100).sumBy { if (a[it][qi] == '1') 1 else 0 }
    }

    val qFromHard = q.withIndex().sortedBy { it.value }

    val cheater = (0 until 100).map { pi ->
        val answersFromHard = qFromHard.map { a[pi][it.index] }

        val anomalies = answersFromHard.subList(0, 10000).withIndex().sumBy { if (it.value == '1') 10000 - it.index else 0 }

        anomalies
    }
        .withIndex()
        .maxByOrNull { it.value }!!
        .index

    println("Case #$t: ${cheater + 1}")
}
