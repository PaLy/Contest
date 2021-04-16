package codejam.s2021.qround.b

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
    val inputs = readLine().split(" ")
    val (x, y) = inputs.subList(0, 2).map { it.toInt() }
    val s = inputs[2]

    val code = mapOf('J' to -1, 'C' to -2, '$' to -3)

    var lastChar = '.'
    val a = mutableListOf(code['$']!!)
    var q = 0

    s.forEach {
        when {
            it == '?' -> q++
            q > 0 -> {
                a += q
                q = 0
                a += code[it]!!
            }
            lastChar != it -> {
                a += code[it]!!
            }
        }
        lastChar = it
    }
    if (q > 0) a += q
    a += code['$']!!

    var cost = 0

    for (i in 1 until a.size - 1) {
        val prev = a[i - 1]
        val cur = a[i]
        val next = a[i + 1]

        when {
            cur > 0 -> {
                when {
                    prev == code['$'] -> {
                        when (next) {
                            code['C'] -> {
                                cost += arrayOf(0, y, cur / 2 * (x + y), y + (cur - 1) / 2 * (x + y)).minOrNull()!!
                            }
                            code['J'] -> {
                                cost += arrayOf(0, x, cur / 2 * (x + y), x + (cur - 1) / 2 * (x + y)).minOrNull()!!
                            }
                        }
                    }
                    next == code['$'] -> {
                        when (prev) {
                            code['C'] -> {
                                cost += arrayOf(0, x, cur / 2 * (x + y), x + (cur - 1) / 2 * (x + y)).minOrNull()!!
                            }
                            code['J'] -> {
                                cost += arrayOf(0, y, cur / 2 * (x + y), y + (cur - 1) / 2 * (x + y)).minOrNull()!!
                            }
                        }
                    }
                    prev == code['C'] -> {
                        when (next) {
                            code['C'] -> {
                                cost += arrayOf(0, (cur + 1) / 2 * (x + y)).minOrNull()!!
                            }
                            code['J'] -> {
                                cost += arrayOf(x, x + (cur / 2) * (x + y)).minOrNull()!!
                            }
                        }
                    }
                    prev == code['J'] -> {
                        when (next) {
                            code['C'] -> {
                                cost += arrayOf(y, y + (cur / 2) * (x + y)).minOrNull()!!
                            }
                            code['J'] -> {
                                cost += arrayOf(0, (cur + 1) / 2 * (x + y)).minOrNull()!!
                            }
                        }
                    }
                }
            }
            cur == code['J'] -> {
                when (prev) {
                    code['C'] -> {
                        cost += x
                    }
                }
            }
            cur == code['C'] -> {
                when (prev) {
                    code['J'] -> {
                        cost += y
                    }
                }
            }
        }
    }

    println("Case #$t: $cost")
}
