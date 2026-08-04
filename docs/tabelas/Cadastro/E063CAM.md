# E063CAM

## Descrição

Tabelas - Cadastros - Câmera de Pesagem de Carga.

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCam | Number(004,0) | Não | Código da Câmera |
| CodExt | String(100) | Sim | Código da câmera no sistema externo ao ERP |
| DesCam | String(100) | Não | Descrição da Câmera |
| UrlCam | String(255) | Não | Endereço URL da Câmera |
| SitCam | String(001) | Não | Situação da Câmera de Pesagem de Carga |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
