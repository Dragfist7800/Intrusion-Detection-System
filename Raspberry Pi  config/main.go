// main.go
// This program is to convert raspberry pi into a server
package main

import (
    "fmt"
    "net/http"
)

func main() {
    // Register handler for default route
    http.HandleFunc("/", HelloHandler)

    // Start server listening
    fmt.Println("Listening on port 4567...")
    err := http.ListenAndServe(":4567", nil)
    if err != nil {
        panic(err)
    }

}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Harshil !", r.URL.Path[1:])
}