# R304COD

## Descrição

e-Sfinge Online - Documentos do Concurso/Processo Seletivo

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NomArq | String(100) | Não | Nome do arquivo relacionado a Atualização do Cargo ou Função |
| SeqReg | Number(009,0) | Não | Sequência |
| NatArq | Number(002,0) | Não | Natureza do Arquivo Texto |
| UrlArq | String(1000) | Sim | URL do Arquivo (se disponível online) |
| CamArq | String(1000) | Sim | Diretório do Arquivo Local |
| ArqDoc | Image | Sim | Arquivo do documento |
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
- NomArq
- SeqReg

---

## Índices

### R304CODIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
