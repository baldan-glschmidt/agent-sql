# E000PRS

## Descrição

Tabelas - Integrações - Processos integrados

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| OriInt | Number(002,0) | Sim | Indica qual o tipo de documento de origem da integração. |
| ChvDoc | String(100) | Sim | Chave da tabela do documento de origem. |
| PrcExe | String(050) | Sim | Indica qual processo de integração foi executado. |
| SitInt | String(050) | Sim | Indica qual a situação da integração. |
| ChvDes | String(100) | Sim | Chave da tabela do documento no sistema integrador. |
| DadInt | String(20000) | Não | Dados enviados para o sistema integrador podendo ser um formato especifico para integração ou texto comum. |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
