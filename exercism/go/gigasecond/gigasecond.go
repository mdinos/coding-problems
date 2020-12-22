// Package gigasecond how far from a given date is a gigasecond away
package gigasecond

// import path for the time package from the standard library
import "time"

// AddGigasecond add a gigasecond to a specific time
func AddGigasecond(t time.Time) time.Time {
	res := t.Add(time.Second * 1000000000)
	return res
}
