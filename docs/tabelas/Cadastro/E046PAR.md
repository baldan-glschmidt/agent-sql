# E046PAR

## Descrição

Tabelas - Visões Contábeis - Parâmetros Processados

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador sequencial dos parâmetros da visão contábil |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| AbrFil | String(4000) | Não | Lista de Abrangência de filiais |
| PerIni | Date | Não | Período inicial do parâmetro |
| PerFim | Date | Não | Período final do parâmetro |
| DesZer | String(001) | Não | Desconsidera Zeramento no cálculo da visão contábil |
| VisPcc | String(001) | Não | Visão por Centro de Custos |
| DatAtu | Date | Não | Data da última atualização nos saldos contábeis |
| HorAtu | Number(005,0) | Não | Hora da última atualização nos saldos contábeis |
| UsuAtu | Number(010,0) | Não | Usuário da última atualização nos saldos contábeis |

---

## Chave Primária

- IdeUni

---

## Índices

### E046PARIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodVis
- AbrFil
- PerIni
- PerFim
- DesZer
- VisPcc

---

## Relacionamentos

### IR_E046PAR_002

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

