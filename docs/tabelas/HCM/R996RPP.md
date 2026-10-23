# R996RPP

## Descrição

Retorno das pendências de integração via processo automático

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeExt | String(255) | Não | Identificador Externo da Requisição |
| NomSis | String(100) | Não | Nome do sistema integrador |
| SerExt | String(255) | Sim | Nome do serviço no sistema integrador |
| SerInt | String(255) | Não | Nome do serviço de integração |
| ConInt | String(19999) | Não | Conteúdo da integração |
| VerInt | Number(003,0) | Sim | Versão da Integração |
| DatCri | Number(012,0) | Não | Data/Hora de criação (Unix) |
| DatPro | Number(012,0) | Não | Data/Hora de processamento (Unix) |
| RetInt | String(19999) | Não | Retorno da integração |
| StsInt | String(020) | Não | Status da integração |

---

## Chave Primária

- IdeUni

---

## Índices

### R996RPPIndice2

**Tipo:** Unico

Campos:
- IdeExt

### R996RPPIndice3

**Tipo:** Não unico

Campos:
- NomSis
- SerExt

### R996RPPIndice4

**Tipo:** Não unico

Campos:
- NomSis
- SerExt
- DatCri
- StsInt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
