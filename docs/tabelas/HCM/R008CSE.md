# R008CSE

## Descrição

Base de Cálculo do Saldo de Eventos

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodSal | Number(004,0) | Não | Código do Saldo |
| CodEve | Number(004,0) | Não | Código do Evento |
| CmpIni | Date | Sim | Competência de Início do Evento para o Saldo |
| SinEve | String(001) | Sim | Sinal do Evento (Soma/Diminui) no Cálculo do Saldo |

---

## Chave Primária

- CodTab
- CodSal
- CodEve

---

## Índices

### R008CSEIndice2

**Tipo:** Não unico

Campos:
- CodTab
- CodEve
- CmpIni

---

## Relacionamentos

### IR_R008CSE_001

**Tabela:** R008CSA

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodSal | CodSal |

### IR_R008CSE_002

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

