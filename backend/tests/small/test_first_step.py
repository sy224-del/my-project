import pytest


@pytest.mark.small
class Givenアプリケーションが起動している場合:
    class Whenヘルスチェックにアクセスすると:
        def then_ヘルスチェックが成功すること(self, client):
            response = client.get("/api/health")

            assert response.status_code == 200
            assert response.json() == {"status": "ok"}

    class Whenメッセージチェックにアクセスすると:
        def then_メッセージが返ってくること(self, client):
            response = client.get("/api/message")

            assert response.status_code == 200
            assert response.json() == {"message": "FastAPIからこんにちは"}
