# R304VRC

## Descrição

e-Sfinge Online - Reserva de Vagas do Resultado do Concurso - Complemento

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
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| NumCpf | Number(011,0) | Não | Número do CPF |
| NumIns | String(016) | Não | Número da Inscrição |
| TipRes | Number(002,0) | Não | Tipo de Reserva de Vagas |
| SeqReg | Number(009,0) | Não | Sequência |
| OrdRes | Number(007,0) | Sim | Ordem de Classificação na Reserva de Vagas |
| PidSta | String(030) | Sim | Pid Status |

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

### R304VRCIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
