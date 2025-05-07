# Keycloak and Plone 🚀

[![Built with Cookieplone](https://img.shields.io/badge/built%20with-Cookieplone-0083be.svg?logo=cookiecutter)](https://github.com/plone/cookieplone-templates/)
[![CI](https://github.com/collective/keycloak-and-plone/actions/workflows/main.yml/badge.svg)](https://github.com/collective/keycloak-and-plone/actions/workflows/main.yml)

Code used during [Plone Hands On: Single Sign-On with Keycloak](https://plone.org/news-and-events/events/plone-hands-on/single-sign-on-with-keycloak) session.

**This should be used for demo/testing purposes only**

## Quick Start 🏁

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [nvm](https://6.docs.plone.org/install/create-project-cookieplone.html#nvm)
-   [Node.js and pnpm](https://6.docs.plone.org/install/create-project.html#node-js) 22
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)


### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/keycloak-and-plone.git
    cd keycloak-and-plone
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Fire Up the Servers 🔥

1.  Start Keycloak and LDAP

    ```shell
    make stack-start
    ```

2.  Create a new Plone site on your first run.

    ```shell
    make backend-create-site
    ```

3.  Start the backend at http://localhost:8080/.

    ```shell
    make backend-start
    ```

4.  In a new shell session, start the frontend at http://localhost:3000/.

    ```shell
    make frontend-start
    ```

Voila! Your Plone site should be live and kicking! 🎉


## Credits and Acknowledgements 🙏

Generated using [Cookieplone (0.9.7)](https://github.com/plone/cookieplone) and [cookieplone-templates (27a6b7b)](https://github.com/plone/cookieplone-templates/commit/27a6b7bd7b0ba9a77b04109d73c4ee975ab95cc3) on 2025-05-06 18:37:31.791865. A special thanks to all contributors and supporters!
