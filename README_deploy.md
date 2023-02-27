# How to deploy on `Render`

> This document should contains all the steps to deploy the app on render without much effort, using PostgreSQL

https://render.com/docs/deploy-django

## ALL STEPS below

<br />

### 👉 Create `PostgreSQL` database on render
  - Go to https://dashboard.render.com/new/database this link.
  - Database name should be `berry`.
  - Keep the Database, User and Datadog API Key as it is.
  - If you want to change database name anything else then you have to change your `render.yaml` file database name too.

<br />

### 👉 Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
  - Click `New Blueprint Instance` button.
  - Connect your `repo` which you want to deploy.
  - Fill the `Service Group Name` and click on `Update Existing Resources` button.
  - After that your deployment will start automatically.