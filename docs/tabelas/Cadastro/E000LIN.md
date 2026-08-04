# E000LIN

## Descrição

Tabelas - Integrações - Log de Integração Receituário Agronômico

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| EndApi | String(400) | Não | Indica a API de acesso para envio/retorno da integração |
| CodInt | Number(001,0) | Não | Código do sistema integrador |
| DatInt | Date | Sim | Data da última integração |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última integração |
| StaInt | String(001) | Sim | Status da integração |
| MsgInt | String(400) | Sim | Mensagem de retorno da integração |
| TipRin | Number(002,0) | Sim | Tipo da informação recebida na integração |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LINIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- EndApi
- DatInt

### E000LINIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodInt

### E000LINIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- TipRin

---

## Relacionamentos

Nenhum relacionamento cadastrado.
