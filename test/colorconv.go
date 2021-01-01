package main

import (
	"fmt"
	"math"
)

const (
	// BLACK the black const
	BLACK = 20.0
	// YELLOW the yellow const
	YELLOW = 70.0
)

func maxmin(val, max, min float64) float64 {
	if val > max {
		val = max
	}
	if val < min {
		val = min
	}
	return val
}

// RGB2Lab convert RGB to Lab
func RGB2Lab(R, G, B float64) []float64 {
	var X, Y, Z, fX, fY, fZ float64
	var L, a, b float64
	// photoshop 默认的转换条件为：srgb and gamma2.2
	r1 := R / 255.0
	g1 := G / 255.0
	b1 := B / 255.0
	// gamma 2.2
	if r1 > 0.04045 {
		r1 = math.Pow((r1+0.055)/1.055, 2.4)
	} else {
		r1 = r1 / 12.92
	}
	if g1 > 0.04045 {
		g1 = math.Pow((g1+0.055)/1.055, 2.4)
	} else {
		g1 = g1 / 12.92
	}
	if b1 > 0.04045 {
		b1 = math.Pow((b1+0.055)/1.055, 2.4)
	} else {
		b1 = b1 / 12.92
	}
	// sRGB
	X = r1*0.436052025 + g1*0.385081593 + b1*0.143087414
	Y = r1*0.222491598 + g1*0.716886060 + b1*0.060621486
	Z = r1*0.013929122 + g1*0.097097002 + b1*0.714185470
	// XYZ range: 0~100
	X = X * 100.0
	Y = Y * 100.0
	Z = Z * 100.0
	// Reference White Point
	//2度视场 D50光源三刺激值
	refX := 96.4221
	refY := 100.0
	refZ := 82.5211
	X = X / refX
	Y = Y / refY
	Z = Z / refZ

	// Lab
	if X > 0.008856 {
		fX = math.Pow(X, 1/3.0)
	} else {
		fX = (7.787 * X) + (16 / 116.0)
	}
	if Z > 0.008856 {
		fZ = math.Pow(Z, 1/3.0)
	} else {
		fZ = (7.787 * Z) + (16 / 116.0)
	}
	if Y > 0.008856 {
		fY = math.Pow(Y, 1/3.0)
		L = (116.0 * fY) - 16.0 + 0.5
	} else {
		fY = (7.787 * Y) + (16 / 116.0)
		L = 903.3 * Y
	}

	a = 500.0*(fX-fY) + 0.5
	b = 200.0*(fY-fZ) + 0.5

	// X = 0.412453*R + 0.357580*G + 0.180423*B
	// Y = 0.212671*R + 0.715160*G + 0.072169*B
	// Z = 0.019334*R + 0.119193*G + 0.950227*B
	// X /= (255 * 0.950456)
	// Y /= 255.0
	// Z /= (255 * 1.088754)

	// if Y > 0.008856 {
	// 	fY = math.Pow(Y, 1.0/3.0)
	// 	L = 116.0*fY - 16.0
	// } else {
	// 	fY = 7.787*Y + 16.0/116.0
	// 	L = 903.3 * Y
	// }

	// if X > 0.008856 {
	// 	fX = math.Pow(X, 1.0/3.0)
	// } else {
	// 	fX = 7.787*X + 16.0/116.0
	// }

	// if Z > 0.008856 {
	// 	fZ = math.Pow(Z, 1.0/3.0)
	// } else {
	// 	fZ = 7.787*Z + 16.0/116.0
	// }
	// a = 500.0 * (fX - fY)
	// b = 200.0 * (fY - fZ)

	// if L < BLACK {
	// 	a *= math.Exp((L - BLACK) / (BLACK / 4))
	// 	b *= math.Exp((L - BLACK) / (BLACK / 4))
	// 	L = BLACK
	// }
	// if b > YELLOW {
	// 	b = YELLOW
	// }
	var ret = make([]float64, 3)
	ret[0] = L
	ret[1] = a
	ret[2] = b
	return ret
}

// Lab2RGB convert Lab to RGB
func Lab2RGB(L, a, b float64) []float64 {
	var X, Y, Z, fX, fY, fZ float64
	var RR, GG, BB float64

	fY = math.Pow((L+16.0)/116.0, 3.0)
	if fY < 0.008856 {
		fY = L / 903.3
	}

	Y = fY

	if fY > 0.008856 {
		fY = math.Pow(fY, 1.0/3.0)
	} else {
		fY = 7.787*fY + 16.0/116.0
	}
	fX = a/500.0 + fY
	if fX > 0.008856 {
		X = math.Pow(fX, 3.0)
	} else {
		X = (fX - 16.0/116.0) / 7.787
	}
	fZ = fY - b/200.0
	if fZ > 0.008856 {
		Z = math.Pow(fZ, 3.0)
	} else {
		Z = (fZ - 16.0/116.0) / 7.787
	}

	// X *= (0.950456 * 255)
	// Y *= 255.0
	// Z *= (1.088754 * 255)
	refX := 96.4221 / 100 * 255
	refY := 100.0 / 100 * 255
	refZ := 82.5211 / 100 * 255
	X *= refX
	Y *= refY
	Z *= refZ

	RR = 3.240479*X - 1.537150*Y - 0.498535*Z
	GG = -0.969256*X + 1.875992*Y + 0.041556*Z
	BB = 0.055648*X - 0.204043*Y + 1.057311*Z

	R := maxmin(RR, 255, 0)
	G := maxmin(GG, 255, 0)
	B := maxmin(BB, 255, 0)
	var ret = make([]float64, 3)
	ret[0] = R
	ret[1] = G
	ret[2] = B
	return ret
}

func main() {
	r1 := RGB2Lab(0, 0, 255)
	// todo: Lab2RGB
	fmt.Println(r1)
	fmt.Println(Lab2RGB(r1[0], r1[1], r1[2]))
}
