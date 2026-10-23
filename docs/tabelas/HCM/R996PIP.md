# R996PIP

## Descrição

Pendências de integração via processo automático

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 2
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

---

## Chave Primária

- IdeUni

---

## Índices

### R996PIPIndice2

**Tipo:** Unico

Campos:
- IdeExt

### R996PIPIndice3

**Tipo:** Não unico

Campos:
- NomSis
- SerExt
- DatCri

---

## Relacionamentos

Nenhum relacionamento cadastrado.
