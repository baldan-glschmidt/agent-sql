# R060QUI

## Descrição

Definições do Quiosque

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| SenAdm | String(010) | Sim | Senha do Administrador. |
| SenPor | String(010) | Sim | Senha da Portaria |
| ModEsp | String(011) | Sim | Modelo de Espelho de Ponto |
| ModBho | String(011) | Sim | Modelo para Consulta de Banco de Horas |
| ModTHo | String(011) | Sim | Modelo Consulta Total Horas |
| CadCra | String(001) | Sim | Consultar Quiosque por Cadastro ou Crachá. |
| ConSen | String(001) | Sim | Consistir Senha na seleção do Colaborador |
| PerDig | String(001) | Sim | Permitir Digitar Crachá (Qdo usa Leitora de Crachá) |
| SenSai | String(001) | Sim | Senha na Saída da Tela |
| SolEmp | String(001) | Sim | Solicitar Empresa |
| TmpExe | Number(002,0) | Sim | Tempo de Execução (segundos) |
| ConSit | String(001) | Sim | Consulta Situações Colaborador |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R060QUI_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

