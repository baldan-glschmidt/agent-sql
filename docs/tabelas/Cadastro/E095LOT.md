# E095LOT

## Descrição

Cadastros - Lotação Tributária

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodLlt | String(030) | Não | Código da lotação |
| DesLot | String(100) | Sim | Descrição da Lotação |
| TipLot | Number(002,0) | Não | Tipo Lotação |
| CodFps | Number(003,0) | Não | Código FPAS |
| CodTer | Number(004,0) | Não | Código de Terceiros Referente ao FPAS |
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

### E095LOTIndice1

**Tipo:** Unico

Campos:
- CodLlt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
