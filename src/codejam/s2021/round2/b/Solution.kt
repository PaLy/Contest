package codejam.s2021.round2.b

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

    val primes = emptyList<Int>().toMutableList()
    var x = n
    for (i in 2..n) {
        if (x % i == 0 && i > 2) {
            primes.add(i)
        }
//        var c = 0
//        while (x % i == 0) {
//            c += 1
//            x /= i
//            if (c == 1) {
//                if (i != 2) {
//                    primes.add(i)
//                }
//            } else if (c == 2) {
//                if (i == 2) {
//                    primes.add(i * c)
//                }
//            }
//        }
//        if (x == 1) {
//            break
//        }
    }

    var res = 1
    for (p in primes) {
        res = maxOf(res, count(n / p))
    }

    println("Case #$t: $res")
}

val counts = emptyMap<Int, Int>().toMutableMap()

fun count(x: Int): Int {
    if (x == 1) return 1
    if (x == 2) return 1
    if (counts.contains(x)) return counts[x]!!

    var res = 1
    for (i in 2 until x) {
        if ((x - 1) % i == 0) {
            res = maxOf(res, 1 + count((x - 1) / i))
        }
    }
    counts[x] = res
    return res
}
