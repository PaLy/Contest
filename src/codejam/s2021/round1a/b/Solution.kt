package codejam.s2021.round1a.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.math.max

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
    val m = readLine().toInt()
    val p = listOf<Int>().toMutableList()
    val n = listOf<Int>().toMutableList()
    for (i in 1..m) {
        val (pi, ni) = readLine().split(" ").map { it.toInt() }
        p += pi
        n += ni
    }

    val maxSum = 499 * 100

    var result = 0

    for (s in 2..maxSum) {
        var sum = 0
        var product = 1
        var ss = s
        for (i in 0 until m) {
            for (j in 1..n[i]) {
                if (ss % p[i] == 0) {
                    product *= p[i]
                    ss /= p[i]
                } else {
                    sum += p[i]
                }
            }
        }
        if (ss == 1 && sum == product) {
            result = max(result, s)
        }
    }

    println("Case #$t: $result")
}
