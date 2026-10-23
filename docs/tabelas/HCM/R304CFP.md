# R304CFP

## Descrição

e-Sfinge - Componentes da Folha de Pagamento

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCom | String(008) | Não | Código do Componente da Folha de Pagamento Conforme Codificação da Un. Gestora |
| AnoMes | Date | Não | Mês e Ano Criação/Atualização do Componente. |
| SeqReg | Number(009,0) | Não | Sequência |
| NatCom | Number(002,0) | Não | Indica a Natureza de Provento ou Desconto do Componente |
| NatRub | Number(004,0) | Sim | Natureza das Rubricas da Folha de Pagamento do sistema eSocial |
| DesCom | String(100) | Não | Descrição do Componente da Folha de Pagamento |
| BasLeg | String(100) | Não | Descrição do Texto Legal que Embasa a Vigência do Componente Salarial |
| IndCom | String(001) | Não | Indicador de Componente (P = Permanente ou E = Eventual) |
| CodTab | Number(003,0) | Sim | Código da Tabela Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- CodCom
- AnoMes
- SeqReg

---

## Índices

### R304CFPIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
