# R126CAN

## Descrição

Requisicoes Vaga Candidato

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Codigo Solicitacao |
| SeqCan | Number(005,0) | Não | Sequência Candidato |
| OriCan | Number(001,0) | Sim | Origem Candidato I,E |
| SitCan | Number(002,0) | Sim | Situação do Candidato |
| NumCan | Number(007,0) | Sim | Numero Candidato |
| NumEmp | Number(004,0) | Sim | Empresa |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Candidato Interno |
| OriSel | Number(001,0) | Sim | Origem Seleção |
| ValSal | Number(013,4) | Sim | Valor do Salário Efetivo |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato |
| MotInt | Number(002,0) | Sim | Motivo da Eliminação do Candidato Interno |
| MotExt | Number(002,0) | Sim | Motivo da Eliminação do Candidato Externo |
| QtdPts | Number(005,0) | Sim | Pontuação obtida no processo seletivo |
| MotCan | String(300) | Sim | Motivo do Cancelamento da Efetivação |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| CodEsc | Number(009,0) | Sim | Código da Escala |

---

## Chave Primária

- CodRqu
- SeqCan

---

## Índices

### R126CANIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

### IR_R126CAN_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

