# E050CTD

## Descrição

Cadastros - Tributos - Código tributação da DESIF

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTri | String(050) | Não | Código |
| DesTri | String(255) | Não | Descrição |
| SerImp | String(010) | Sim | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |
| CodFim | String(020) | Sim | Código fiscal municipal |
| CodRai | Number(007,0) | Sim | Código da cidade RAIS utilizada para apuração do ISS |
| VigIni | Date | Sim | Data do Início da Vigência |
| PerIss | Number(015,2) | Sim | Percentual do ISSQN |

---

## Chave Primária

- IdeUni

---

## Índices

### E050CTD_FKIndex1

**Tipo:** Não unico

Campos:
- CodRai

### E050CTD_Indice2

**Tipo:** Unico

Campos:
- CodEmp
- CodTri
- VigIni
- CodRai

---

## Relacionamentos

Nenhum relacionamento cadastrado.
