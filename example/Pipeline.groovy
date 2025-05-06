package example

class Pipeline {
    static def deployFlaskApp(script) {
        script.bat '''
            call venv\\Scripts\\activate
            gunicorn app:app
        '''
    }
}