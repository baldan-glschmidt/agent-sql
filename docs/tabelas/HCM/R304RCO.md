# R304RCO

## Descrição

e-Sfinge Online - Relação da Convocação do Concurso

---

## Resumo

- Campos: 13
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| DatCon | Date | Não | Data da Convocação |
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| NumCpf | Number(011,0) | Não | Número do CPF |
| NumIns | String(016) | Não | Número da Inscrição |
| SeqReg | Number(009,0) | Não | Sequência |
| TipCon | Number(002,0) | Não | Tipo de convocação |
| OrdCon | Number(007,0) | Não | Ordem que se deu a convocação para a posse, levando em consideração a classificação geral e reserva de vagas especiais |
| PidSta | String(030) | Sim | Pid Status |

---

## Chave Primária

- NumEmp
- NumEdi
- DatCon
- NumEsp
- TipQua
- CarFun
- DatIni
- NumCpf
- NumIns
- SeqReg

---

## Índices

### R304RCOIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
