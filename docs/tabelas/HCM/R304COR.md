# R304COR

## Descrição

e-Sfinge Online - Resultados do Concurso/Processo Seletivo

---

## Resumo

- Campos: 26
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| NumCpf | Number(011,0) | Não | Número do CPF |
| SeqReg | Number(009,0) | Não | Sequência |
| NumIns | String(016) | Não | Número da Inscrição |
| NomApr | String(100) | Não | Nome do Aprovado |
| OrdGer | Number(007,0) | Não | Ordem da Classificação Geral |
| TipRes | Number(002,0) | Sim | Tipo de Reserva de Vagas |
| OrdRes | Number(007,0) | Sim | Ordem de Classificação na Reserva de Vagas |
| NotFin | Number(007,4) | Não | Nota Final do Aprovado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
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
- NumEdi
- NumEsp
- TipQua
- CarFun
- DatIni
- NumCpf
- NumIns
- SeqReg

---

## Índices

### R304CORIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
