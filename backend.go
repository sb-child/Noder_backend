package main

import (
	"fmt"
	"net/http"

	socketio "github.com/googollee/go-socket.io"
)

// NdServer server.
type NdServer struct {
	sktMux    *http.ServeMux
	sktServer *http.Server
	sktIoSrv  *socketio.Server
}

func (srv *NdServer) init(addr string) {
	srv.sktIoSrv = socketio.NewServer(nil)
	srv.sktMux = http.NewServeMux()
	srv.sktServer = &http.Server{}
	srv.sktServer.Addr = addr
	srv.sktMux.Handle("/socket.io/", srv.sktIoSrv)
	srv.sktServer.Handler = srv.sktMux
}
func (srv *NdServer) start() {
	srv.sktServer.ListenAndServe()
}
func main() {
	// todo: replace socket.io to other
	a := NdServer{}
	a.init("0.0.0.0:37321")
	a.sktIoSrv.OnConnect("", func(conn socketio.Conn) error {
		fmt.Println(conn.ID())
		return nil
	})
	a.start()
	fmt.Println("hello")
	b := "2343" + "1111"
	b += "222"
	fmt.Println(b)
}
