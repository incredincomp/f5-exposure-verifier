"""Authentication configuration.

Auth configuration is currently provided by the ``Settings`` fields
(``api_key``, ``api_key_header``) in ``app.config.settings``.

This module is the intended home for dedicated auth configuration logic
(e.g. multiple key tiers, OIDC config) once auth is hardened beyond the
current basic API-key stub in ``app.api.auth``.
"""
