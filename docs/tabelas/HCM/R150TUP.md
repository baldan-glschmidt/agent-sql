# R150TUP

## Descrição

Versões dos Termos de Consentimento

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTer | Number(002,0) | Não | Código do termo de consentimento |
| CodVer | Number(004,0) | Não | Código da versão do termo de consentimento |
| TitTup | String(100) | Sim | Título da versão do termo de consentimento |
| SitTUP | Number(001,0) | Sim | Situação da versão do termo de consentimento |
| DatHor | Number(014,6) | Sim | Data e Hora que a versão foi publicada. |
| CodUsu | Number(010,0) | Não | Código do Usuário que publicou a versão do termo de consentimento |
| ReqAce | String(001) | Sim | Informar se a publicação desta versão requer um novo aceite para disponibilização das informações |
| UltVer | Number(004,0) | Sim | Informar a última versão em que o aceite é válido para disponibilização das informações |
| TexTer | String(50000) | Sim | Texto do termo de consentimento |
| TexRec | String(1000) | Sim | Mensagem de confirmação de recusa |
| TexAce | String(1000) | Sim | Mensagem de confirmação de aceite |
| CamAux1 | String(001) | Sim | Campo Auxiliar 1 |
| CamAux2 | Date | Sim | Campo Auxiliar 2 |
| CamAux3 | Number(010,0) | Sim | Campo Auxiliar 3 |

---

## Chave Primária

- CodTer
- CodVer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
