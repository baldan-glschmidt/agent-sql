# R304RRV

## Descrição

e-Sfinge Online - Reserva de Vagas Especiais do Concurso/Processo Seletivo

---

## Resumo

- Campos: 12
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da especialidade |
| TipQua | Number(002,0) | Não | Tipo de quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de início da vigência do cargo |
| NumCpf | Number(011,0) | Não | Número do CPF |
| NumIns | String(016) | Não | Número da inscrição |
| TipRes | Number(002,0) | Não | Tipo de reserva de vaga |
| SeqReg | Number(009,0) | Não | Sequência |
| OrdCla | Number(007,0) | Sim | Ordem de classificação na reserva de vaga |
| PidSta | String(030) | Sim | Pid status |

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
- TipRes
- SeqReg

---

## Índices

### R304RRVIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
