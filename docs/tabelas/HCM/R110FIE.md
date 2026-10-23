# R110FIE

## Descrição

Ficha Médica - Exames

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodExa | Number(004,0) | Não | Código Exame |
| UsaAdm | String(001) | Sim | Gerar Solicitação Exame p/ Admissional |
| UsaRet | String(001) | Sim | Gerar Solicitação Exame p/ Retorno do Afastamento |
| UsaTlo | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Local |
| UsaTca | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Cargo |
| UsaTfu | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Função |
| UsaDem | String(001) | Sim | Gerar Solicitação Exame p/ Demissional |
| UsaAco | String(001) | Sim | Gerar Solicitação Exame p/ Acompanhamento Demitidos |
| UsaNor | String(001) | Sim | Gerar Solicitação Exame p/ Periódico |
| CodReg | Number(003,0) | Sim | Código da Regra para Exame |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110FIE_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110FIE_002

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

