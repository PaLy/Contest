package codejam.s2022.qround.b

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
    var a = emptyArray<List<Int>>()
    for (i in 1..3) {
        val p = readLine().split(" ").map { it.toInt() }
        a += p
    }

    var mins = emptyArray<Int>()
    for (i in a[0].indices) {
        mins += a.minByOrNull { it[i] }!![i]
    }

    val minsFromMax = mins.withIndex().sortedBy { it.value }.reversed()
    val result = arrayOf(0, 0, 0, 0)
    var left = 1000000
    minsFromMax.forEach {
        result[it.index] = minOf(it.value, left)
        left -= result[it.index]
    }

    if (left == 0) {
        println("Case #${t}: ${result.joinToString(" ")}")
    } else {
        println("Case #${t}: IMPOSSIBLE")
    }
}
