var gulp = require('gulp'),
    browserSync = require('browser-sync').create();

const spawn = require('child_process').spawn;

var reload = browserSync.reload;

// Run the Django development server
gulp.task('run-django-server', function(cb) {
    spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit' });
    cb();
});


gulp.task('copy', function(cb) {
  gulp.src(['node_modules/jquery/dist/jquery.js'])
    .pipe(gulp.dest('ifa_standards_rms/static/vendors/jquery'))
  gulp.src(['node_modules/bootstrap/dist/css/bootstrap.css', 'node_modules/bootstrap/dist/js/bootstrap.js'])
    .pipe(gulp.dest('ifa_standards_rms/static/vendors/bootstrap'))
  cb();
});

gulp.task('browsersync', function(cb) {
    browserSync.init({
        notify: false,
        proxy: "localhost:8000",
        logLevel: 'debug',
        logConnections: true,
        reloadDelay: 300,
        reloadDebounce: 500,
    });
    cb();
});

gulp.task('watch', function(cb) {
    gulp.watch('templates/**/*.html').on('change', reload);
    gulp.watch('static/**/*.(js|css)').on('change', reload);
});

gulp.task('frontend', function(cb) {
    setTimeout(gulp.series('browsersync', 'watch'), 10000);  
});

gulp.task('default', gulp.series('run-django-server', 'frontend'));
