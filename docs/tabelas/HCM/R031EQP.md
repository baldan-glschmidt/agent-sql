# R031EQP

## Descrição

Geração de Escalas - Equipes

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| DesEqp | String(050) | Sim | Descrição da Equipe |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| ResDep | String(050) | Sim | Responsável pelo Departamento |
| ResAre | String(050) | Sim | Responsável pela Área |
| NomSup | String(050) | Sim | Nome do Supervisor |
| TelFPM | String(001) | Sim | Quantidade de Folgas no Mês |
| TelTPM | String(001) | Sim | Quantidade de Trabalhos no Mês |
| TelPAC | String(001) | Sim | Mínimo de Preferências Atendidas Por Colaborador |
| TelFSF | String(001) | Sim | Número Mínimo de Finais de Semana de Folga |
| TelDFo | String(001) | Sim | Número Mínimo de Domingos de Folga |
| TelFFe | String(001) | Sim | Número Mínimo de Folgas em Feriados |
| TelCOB | String(001) | Sim | Coluna Observações |
| TelCor | String(001) | Sim | COREN |
| TelReg | String(001) | Sim | Regime de Trabalho |
| TelTcl | String(001) | Sim | Tipo Colaborador |
| TabFer | Number(004,0) | Sim | Tabela de Feriados |
| TelUFo | String(001) | Sim | Data da Última Folga Mês Anterior |
| TelNCa | String(001) | Sim | Número do Cadastro do Colaborador |

---

## Chave Primária

- CodEqp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031EQP_002

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R031EQP_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

