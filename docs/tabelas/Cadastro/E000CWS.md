# E000CWS

## Descrição

Integrações - Configuração de web service

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqcWS | Number(009,0) | Não | Número sequencial da configuração de web service |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| CodReg | Number(004,0) | Sim | Código da regra |
| WebSer | String(1000) | Não | Web service configurado |
| PorTaa | String(250) | Não | Porta do web service configurado |
| FilTro | String(4000) | Sim | Filtro do web service |

---

## Chave Primária

- SeqcWS

---

## Índices

### E000CWSIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodInt
- WebSer
- PorTaa

---

## Relacionamentos

Nenhum relacionamento cadastrado.
