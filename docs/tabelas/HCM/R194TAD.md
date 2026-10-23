# R194TAD

## Descrição

BS - Adicionais

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAdi | Number(004,0) | Não | Código do Adicional |
| DesAdi | String(030) | Sim | Descrição do Adicional |
| TaxAdi | Number(005,2) | Sim | Taxa do Adicional |
| CodSit | Number(003,0) | Sim | Situação do Adicional |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| AbrSit | String(030) | Sim | Situações a Somar |
| BasAdi | String(001) | Sim | Base Cálculo |
| TipAdi | Number(001,0) | Sim | Tipo Adicional |
| CodTar | Number(004,0) | Sim | Codigo da Tarefa |
| SomDsr | String(001) | Sim | Soma para cálculo do DSR |

---

## Chave Primária

- CodAdi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R194TAD_003

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

