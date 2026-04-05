/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/default-config.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /* Templates within theme app */
        '../templates/**/*.html',

        /* Main templates directory of the project */
        '../../templates/**/*.html',

        /* Templates in other django apps */
        '../../core/templates/**/*.html',
        '../../projects/templates/**/*.html',
        '../../resume/templates/**/*.html',

        /* * Python files: In case you write tailwind classes in your python code (e.g. forms.py)
         */
        '../../**/*.py'
    ],
    theme: {
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}