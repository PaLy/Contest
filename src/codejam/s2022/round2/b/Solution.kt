package codejam.s2022.round2.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.math.round
import kotlin.math.sqrt
import kotlin.math.truncate

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
    val r = readLine().toInt()

    val mWrong = Array(r * 2 + 1) { Array(r * 2 + 1) { 0 } }
    drawCircleFilledWrong(r, mWrong)

    val m = Array(r * 2 + 1) { Array(r * 2 + 1) { 0 } }
    drawCircleFilled(r, m)

    val mWrongCount = count(mWrong)
    val mCount = count(m)
//    println(mWrongCount)
//    println(mCount)
//    if (r < 3) {
//        println(mWrong.joinToString("\n") { it.joinToString(" ") })
//        println("***")
//        println(m.joinToString("\n") { it.joinToString(" ") })
//    }

    val result = mCount - mWrongCount

    println("Case #${t}: $result")
}

fun count(m: Array<Array<Int>>): Int {
    return m.sumOf {
        it.count { it == 1 }
    }
}

fun myRound(y: Double): Int {
    val ty = truncate(y)
    return if (y == ty + 0.5) {
        ty.toInt()
    } else {
        round(y).toInt()
    }
}

fun drawCirclePerimeter(R: Int, r: Int, m: Array<Array<Int>>) {
    for (x in -r..r) {
        val y = myRound(sqrt(r.toDouble() * r - x * x))
        m[R + x][R + y] = 1
        m[R + x][R + -y] = 1
        m[R + y][R + x] = 1
        m[R + -y][R + x] = 1
    }
}

fun drawCircleFilled(r: Int, m: Array<Array<Int>>) {
    for (x in -r..r) {
        for (y in -r..r) {
            if (myRound(sqrt(x.toDouble() * x + y * y)) <= r) {
                m[r + x][r + y] = 1
            }
        }
    }
}

fun drawCircleFilledWrong(r: Int, m: Array<Array<Int>>) {
    for (x in 0..r) {
        drawCirclePerimeter(r, x, m)
    }
}