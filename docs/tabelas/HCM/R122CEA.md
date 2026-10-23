# R122CEA

## Descrição

Candidatos Externos - Empregos Anteriores

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatAdm | Date | Não | Data Admissão |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| CodOem | Number(008,0) | Sim | Empresa Anterior |
| NomOem | String(060) | Sim | Nome da empresa |
| DatDem | Date | Sim | Data Demissão |
| MotDem | Number(003,0) | Sim | Motivo Demissão |
| UltSal | Number(011,2) | Sim | Último Salário Candidato |
| DesMoe | String(005) | Sim | Símbolo Moeda |
| ComEmp | String(1000) | Sim | Comentários sobre o Emprego |
| CodAtu | Number(005,0) | Sim | Código do ramo de atuação da empresa |
| DesAtu | String(060) | Sim | Descrição do ramo de atuação da empresa |
| USU_TemExp | String(001) | Sim | Tem Experiência? |

---

## Chave Primária

- NumCan
- DatAdm
- SeqAdm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CEA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

