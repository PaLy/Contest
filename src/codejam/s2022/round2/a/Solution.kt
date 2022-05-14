package codejam.s2022.round2.a

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

val dx = arrayOf(0, 1, 0, -1)
val dy = arrayOf(1, 0, -1, 0)

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    val (n, k) = readLine().split(" ").map { it.toInt() }

    val d = Array(n * n + 1) { emptyList<Pair<Int, Int>>().toMutableList() }
    for (i in 1..n * n) {
        d[i].add(Pair(i - 1, i - 1))
    }

    val m = fillM(n)

//    println(m.joinToString("\n") { it.joinToString(" ")})

    seqXY(n).forEachIndexed { index, (x, y) ->
        for (dir in 0 until 4) {
            val nx = x + dx[dir]
            val ny = y + dy[dir]
            if (isIn(nx, ny, n) && m[nx][ny] > m[x][y]) {
                val doneKK = d[m[nx][ny]].map { (x) -> x - 1 }.toSet()
                for ((kk) in d[index + 1]) {
                    if (!doneKK.contains(kk)) {
                        d[m[nx][ny]].add(Pair(kk + 1, index + 1))
                    }
                }
            }
        }
    }

    val path = getPath(d, n * n, k)

    if (path.isEmpty()) {
        println("Case #${t}: IMPOSSIBLE")
    } else {
        println("Case #${t}: ${path.size}")
        println(path.reversed().joinToString("\n") { "${it.first} ${it.second}" })
    }
}

fun getPath(d: Array<MutableList<Pair<Int, Int>>>, n: Int, k: Int): List<Pair<Int, Int>> {
    val res = emptyList<Pair<Int, Int>>().toMutableList()
    var curN = n
    var curK = k
    while (curN > 0) {
        val next = d[curN].firstOrNull { (x) -> x == curK }
        if (next == null) {
            break
        } else {
            res.add(Pair(next.second, curN))
            curN = next.second
            curK--
        }
    }
    return res.filter { (x, y) -> x + 1 != y }
}

fun seqXY(n: Int): Array<Pair<Int, Int>> {
    val res = Array(n * n) { Pair(0, 0) }
    val done = emptySet<Int>().toMutableSet()
    var x = 0
    var y = 0
    var d = 0
    for (i in 1..n * n) {
        res[i - 1] = Pair(x, y)
        done.add(x * 10000 + y)
        val nx = x + dx[d]
        val ny = y + dy[d]
        if (isIn(nx, ny, n) && !done.contains(nx * 10000 + ny)) {
            x = nx
            y = ny
        } else {
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]
        }
    }
    return res
}

private fun isIn(nx: Int, ny: Int, n: Int) = nx in 0 until n && ny in 0 until n

fun fillM(n: Int): Array<Array<Int>> {
    val res = Array(n) { Array(n) { 0 } }
    val s = seqXY(n)
    s.forEachIndexed { index, (x, y) ->
        res[x][y] = index + 1
    }
    return res
}
