// Package space contains functions for calculating age dependant on the planet you're on
package space

// Planet is the name of a planet in our solar system
type Planet string

// Age calculates time in planet-years from an input of seconds
func Age(seconds float64, planet Planet) float64 {
	const earthYearInSeconds float64 = 31557600
	yearLengthRelativeToEarth := map[Planet]float64{
		"Mercury": 0.2408467,
		"Venus":   0.61519726,
		"Earth":   1.0,
		"Mars":    1.8808158,
		"Jupiter": 11.862615,
		"Saturn":  29.447498,
		"Uranus":  84.016846,
		"Neptune": 164.79132,
	}

	return  (seconds / earthYearInSeconds) / yearLengthRelativeToEarth[planet]
}
