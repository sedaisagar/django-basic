// Javascript code works here

document.addEventListener( "DOMContentLoaded", () => {
    console.log( "Content Loaded" )
    const url = '/api/services/'

    fetch( url, { headers: { 'method': "GET" } } )
        .then( ir => ir.json() )
        .then( r => {
            // js -> document.getElementById("services-container")
            // jquery -> $( "#services-container" )

            $( "#services-container" ).html( '' )

            // document.getElementById()
            // $( "#services-container" )

            // document.getElementsByClassName()
            // $( ".services-container" )

            // now i have data
            r?.forEach( res => {
                var cont = `
                <div class="col-lg-4 col-md-6">
                    <div
                        class="service-item bg-light rounded d-flex flex-column align-items-center justify-content-center text-center">
                        <div class="service-icon mb-4">
                            <img src="/media/${res?.icon}" height=50 width=50/>
                        </div>
                        <h4 class="mb-3">${res?.title}</h4>
                        <p class="m-0">${res?.short_description}</p>
                        <a class="btn btn-lg btn-primary rounded-pill" href="#!">
                            <i class="bi bi-arrow-right"></i>
                        </a>
                    </div>
                </div>
                `;

                $( "#services-container" ).append( cont )

            } )
        } )

} )